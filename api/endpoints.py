from unittest import result
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .schemas import IdiomRequest, UserAnswerInput, SessionInput, FillingExerciseRequest
from craft_modules.idiom.chains.all_chains import idiom_chain, get_session_history
from craft_modules.idiom.chains.all_chains import matching_chain, extract_chain, evaluate_chain, filling_gap_chain
from craft_modules.idiom.chains.all_chains import extract_idioms_chain, feedback_chain
from api.endpoint_utils import get_idioms_list_from_session


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("frontpage.html", {"request": request})

@router.get("/idiom_craft.html", response_class=HTMLResponse)
async def idiom_craft(request: Request):
    return templates.TemplateResponse("idiom_craft.html", {"request": request})

@router.post("/generate_idioms")
async def generate_idioms(request: Request, body: IdiomRequest):
    inputs = {
        "nbr_idioms": body.nbr_idioms,
        "topic": body.topic,
        "level": body.level
    }

    session_id = getattr(body, 'session_id', 'default')
    session = get_session_history(session_id)
    session.meta["level"] = body.level
    
    response = idiom_chain.invoke(inputs)
    # Add AI response to history
    tagged_msg = "[GENERATE_PROPMPT]\n" + response.content
    session.history.add_ai_message(tagged_msg)
    # updated_history = get_session_history(session_id)
    return {"idioms": response.content}

@router.get("/training", response_class=HTMLResponse)
async def training_room(request: Request):
    return templates.TemplateResponse("full_training.html", {"request": request})

@router.post("/matching_exercise")
async def matching_exercise(request: Request):
    # Get session_id from request body or use default
    body = await request.json()
    session_id = body.get('session_id', 'default')
    
    # Get conversation history using the same function as generate_idioms
    session = get_session_history(session_id)
    if not session.history.messages:
        return {"error": "No conversation history found. Please generate idioms first."}
    # Find the last AI message (idioms response)
    last_response = None
    for msg in reversed(session.history.messages):
        if msg.type == "ai":
            last_response = msg.content
            break

    if not last_response:
        return {"error": "No idioms generated yet. Please generate idioms first."}
    
    try:
        # Extract idioms from the last response
        extracted_idioms = extract_chain.invoke({"text": last_response})
        # Generate matching exercise
        exercise = matching_chain.invoke({
            "idioms": extracted_idioms.content
        })
        # Add the exercise response to history
        tagged_msg = "[MATCHING_PROMPT]\n" + exercise.content
        session.history.add_ai_message(tagged_msg)
        
        return {"exercise": exercise.content}
        
    except Exception as e:
        return {"error": f"Failed to create exercise: {str(e)}"}

@router.post("/evaluate_answer")
async def evaluate_section(body: UserAnswerInput):
    session_id = body.session_id
    user_answer = body.user_answer
    exercise_type = body.exercise_type or "matching"

    if not user_answer.strip():
        return {"error": "No answer provided."}

    session = get_session_history(session_id)

    prefix_map = {
        "matching": "[MATCHING_PROMPT]",
        "filling" : "[FILLING_PROMPT]"
    }

    prefix = prefix_map.get(exercise_type)

    last_exercise =  next(
        (msg.content for msg in reversed(session.history.messages) 
        if msg.type == "ai" and msg.content.startwith(prefix)),
        None
    )

    if not last_exercise:
        return{"error": "No matching exercise found for this session"}
        
    try:
        evaluation = evaluate_chain.invoke({
            "exercise": last_exercise,
            "user_answer": user_answer
        })
        return {"feedback": evaluation.content}
    except Exception as e:
        return {"error": f"Failed to create exercise: {str(e)}"}
    

@router.post("/idioms_list")
async def get_idioms_list(body: SessionInput):
    generate_idioms = get_idioms_list_from_session(body.session_id)
    if not generate_idioms:
        return {"messages:" "No idioms available"}
    return {"exercise": generate_idioms}

@router.post("/creative_game")
async def creative_exercise(body: UserAnswerInput):
    session_id = body.session_id
    user_answer = body.user_answer

    if not user_answer.strip():
        return {"error": "No answer provided."}

    session = get_session_history(session_id)
    matching_response = next(
        (msg.content for msg in reversed(session.history.messages)
            if msg.type == "ai" and msg.content.startswith("[MATCHING_PROMPT]")),
            None
    )
    try:
        extracted_idioms_list = extract_idioms_chain.invoke({"text": matching_response})
        feedback = feedback_chain.invoke({
            "idioms": extracted_idioms_list.content,
            "text": user_answer
        })
        return {"feedback": feedback.content}
    except Exception as e:
        return {"error": f"Failed to create exercise: {str(e)}"}

@router.post("/filling_exercise")
async def generate_filling_exercise(body: FillingExerciseRequest):
    generated_idioms = get_idioms_list_from_session(body.session_id)
    if not generated_idioms:
        return {"message": "No idioms available"}

    # Optional: Store user's answer for later evaluation
    session = get_session_history(body.session_id)
    session.meta["user_answer"] = body.user_answer

    # You also need the level — retrieve it from session metadata or history
    level = session.meta.get("level")
    if not level:
        return {"error": "Missing level information"}

    filling_exercise = filling_gap_chain.invoke({
        "idioms": generated_idioms,
        "level": level
    })
    # Add the exercise response to history
    tagged_msg = "[FILLING_PROMPT]\n" + filling_exercise.content
    return {"exercise": filling_exercise.content}

api_router = router
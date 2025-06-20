from unittest import result
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .schemas import IdiomRequest, UserAnswerInput, SessionInput
from idiomCraft.chains.all_chains import idiom_chain, get_session_history
from idiomCraft.chains.all_chains import matching_chain, extract_chain, evaluate_chain
from idiomCraft.chains.all_chains import extract_idioms_chain, feedback_chain


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate_idioms")
async def generate_idioms(request: Request, body: IdiomRequest):
    inputs = {
        "nbr_idioms": body.nbr_idioms,
        "topic": body.topic,
        "level": body.level
    }
    session_id = getattr(body, 'session_id', 'default')
    current_history = get_session_history(session_id)
    response = idiom_chain.invoke(inputs)
    # Add AI response to history
    tagged_msg = "[GENERATE_PROPMPT]\n" + response.content
    current_history.add_ai_message(tagged_msg)
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
    current_history = get_session_history(session_id)
    if not current_history.messages:
        return {"error": "No conversation history found. Please generate idioms first."}
    # Find the last AI message (idioms response)
    last_response = None
    for msg in reversed(current_history.messages):
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
        current_history.add_ai_message(tagged_msg)
        
        return {"exercise": exercise.content}
        
    except Exception as e:
        return {"error": f"Failed to create exercise: {str(e)}"}

@router.post("/evaluate_answer")
async def evaluate_section(body: UserAnswerInput):
    session_id = body.session_id
    user_answer = body.user_answer

    if not user_answer.strip():
        return {"error": "No answer provided."}

    current_history = get_session_history(session_id)

    last_exercise =  next(
        (msg.content for msg in reversed(current_history.messages) if msg.type == "ai"),
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
    
@router.post("/idioms-list")
async def get_idioms_list(body: SessionInput):
    session_id = body.session_id
    history = get_session_history(session_id)

    # Find the last AI message containing idioms
    last_idioms = next(
        (msg.content for msg in reversed(history.messages)
              if msg.type == "ai" and msg.content.startswith("[MATCHING_PROMPT]")),
        None
    )

    if not last_idioms:
        return {"error": "No idioms found. Do matching exercise first."} 
    extracted_idioms_list = extract_idioms_chain.invoke({"text": last_idioms})
    return {"exercise": extracted_idioms_list.content}

@router.post("/creative_game")
async def creative_exercise(body: UserAnswerInput):
    session_id = body.session_id
    user_answer = body.user_answer

    if not user_answer.strip():
        return {"error": "No answer provided."}

    current_history = get_session_history(session_id)
    matching_response = next(
        (msg.content for msg in reversed(current_history.messages)
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
    

api_router = router
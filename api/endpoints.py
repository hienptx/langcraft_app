from unittest import result
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .schemas import IdiomRequest
from idiomCraft.chains.chains import idiom_chain, get_session_history
from idiomCraft.chains.chains import matching_chain, extract_chain

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
    
    # # Print history BEFORE making the request
    # print(f"\n=== CONVERSATION HISTORY FOR SESSION: {session_id} ===")
    current_history = get_session_history(session_id)
    # if current_history.messages:
    #     for i, msg in enumerate(current_history.messages, 1):
    #         msg_type = "USER" if msg.type == "human" else "ASSISTANT"
    #         print(f"{i}. {msg_type}: {msg.content}")
    # else:
    #     print("No previous conversation history.")
    # print("=" * 50)
    
    # Invoke the chain
    response = idiom_chain.invoke(inputs)
    
    # Add AI response to history
    current_history.add_ai_message(response.content)
    
    # Print history AFTER making the request
    # print(f"\n=== UPDATED HISTORY FOR SESSION: {session_id} ===")
    updated_history = get_session_history(session_id)
    # for i, msg in enumerate(updated_history.messages, 1):
    #     msg_type = "USER" if msg.type == "human" else "ASSISTANT"
    #     print(f"{i}. {msg_type}: {msg.content}")
    # print("=" * 50)
    return {"idioms": response.content}

@router.get("/training", response_class=HTMLResponse)
async def training_room(request: Request):
    return templates.TemplateResponse("training.html", {"request": request})

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
            "idioms": extracted_idioms.content,
            "user_answer": "Create a matching exercise for these idioms."
        })
        # Add the exercise request and response to history
        # current_history.add_user_message("Create a matching exercise for the generated idioms")
        current_history.add_ai_message(exercise.content)
        
        return {"exercise": exercise.content}
        
    except Exception as e:
        return {"error": f"Failed to create exercise: {str(e)}"}

# @router.post("/evaluate_answer")


api_router = router
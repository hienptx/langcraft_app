from typing import Optional
from craft_modules.idiom.chains.all_chains import evaluate_chain, extract_idioms_chain, get_session_history

def get_idioms_list_from_session(session_id: str) -> Optional[str]:
    session = get_session_history(session_id)

    # Find the last AI message containing idioms
    last_idioms = next(
        (msg.content for msg in reversed(session.history.messages)
              if msg.type == "ai" and msg.content.startswith("[MATCHING_PROMPT]")),
        None
    )

    if not last_idioms:
        return None
     
    extracted_idioms_list = extract_idioms_chain.invoke({"text": last_idioms})
    return extracted_idioms_list.content
# from unittest import result
# from fastapi import FastAPI, APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from .schemas import IdiomRequest, UserAnswerInput, SessionInput
# from craft_modules.idiom.chains.all_chains import idiom_chain, get_session_history
# from craft_modules.idiom.chains.all_chains import matching_chain, extract_chain, evaluate_chain
# from craft_modules.idiom.chains.all_chains import extract_idioms_chain, feedback_chain


# router = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @router.get("/", response_class=HTMLResponse)
# async def read_index(request: Request):
#     return templates.TemplateResponse("frontpage.html", {"request": request})

# # // LangCraft API Endpoints Structure
# # // Base URL: https://api.langcraft.com/v1

# # // ==========================================
# # // AUTHENTICATION ENDPOINTS
# # // ==========================================

# # // POST /auth/login
# # // Login user with email and password

# const loginEndpoint = {
#     method: 'POST',
#     url: '/auth/login',
#     headers: {
#         'Content-Type': 'application/json'
#     },
#     body: {
#         email: 'user@example.com',
#         password: 'userpassword'
#     },
#     response: {
#         success: true,
#         data: {
#             token: 'jwt_token_here',
#             user: {
#                 id: 123,
#                 email: 'user@example.com',
#                 name: 'John Doe',
#                 level: 'intermediate',
#                 streak: 5
#             }
#         }
#     }
# };

# # // POST /auth/register
# # // Register new user
# const registerEndpoint = {
#     method: 'POST',
#     url: '/auth/register',
#     body: {
#         name: 'John Doe',
#         email: 'user@example.com',
#         password: 'userpassword',
#         language_preference: 'spanish'
#     }
# };

# # // POST /auth/logout
# # // Logout user
# const logoutEndpoint = {
#     method: 'POST',
#     url: '/auth/logout',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     }
# };

# # // ==========================================
# # // USER PROFILE ENDPOINTS
# # // ==========================================

# # // GET /user/profile
# # // Get user profile information
# const getUserProfile = {
#     method: 'GET',
#     url: '/user/profile',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     response: {
#         success: true,
#         data: {
#             id: 123,
#             name: 'John Doe',
#             email: 'user@example.com',
#             level: 'intermediate',
#             streak: 5,
#             total_lessons: 45,
#             words_learned: 234,
#             preferred_language: 'spanish'
#         }
#     }
# };

# # // PUT /user/profile
# # // Update user profile
# const updateUserProfile = {
#     method: 'PUT',
#     url: '/user/profile',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'application/json'
#     },
#     body: {
#         name: 'John Smith',
#         preferred_language: 'french'
#     }
# };

# # // ==========================================
# # // IDIOM CRAFT ENDPOINTS
# # // ==========================================

# # // GET /idiom-craft/lessons
# # // Get list of idiom lessons
# const getIdiomLessons = {
#     method: 'GET',
#     url: '/idiom-craft/lessons',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         language: 'spanish',
#         level: 'beginner',
#         page: 1,
#         limit: 10
#     },
#     response: {
#         success: true,
#         data: {
#             lessons: [
#                 {
#                     id: 1,
#                     title: 'Common Spanish Idioms',
#                     description: 'Learn everyday Spanish expressions',
#                     difficulty: 'beginner',
#                     idioms_count: 15,
#                     completed: false
#                 }
#             ],
#             total: 25,
#             page: 1,
#             pages: 3
#         }
#     }
# };

# # // GET /idiom-craft/lesson/:id
# # // Get specific idiom lesson content
# const getIdiomLesson = {
#     method: 'GET',
#     url: '/idiom-craft/lesson/1',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     response: {
#         success: true,
#         data: {
#             id: 1,
#             title: 'Common Spanish Idioms',
#             idioms: [
#                 {
#                     id: 1,
#                     phrase: 'estar en las nubes',
#                     meaning: 'to be distracted or absent-minded',
#                     example: 'María está en las nubes durante la clase.',
#                     translation: 'Maria is absent-minded during class.'
#                 }
#             ]
#         }
#     }
# };

# # // POST /idiom-craft/progress
# # // Submit idiom lesson progress
# const submitIdiomProgress = {
#     method: 'POST',
#     url: '/idiom-craft/progress',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'application/json'
#     },
#     body: {
#         lesson_id: 1,
#         completed_idioms: [1, 2, 3],
#         score: 85,
#         time_spent: 300 // seconds
#     }
# };

# # // ==========================================
# # // CONVERSATION CRAFT ENDPOINTS
# # // ==========================================

# # // GET /conversation-craft/scenarios
# # // Get conversation scenarios
# const getConversationScenarios = {
#     method: 'GET',
#     url: '/conversation-craft/scenarios',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         language: 'spanish',
#         level: 'intermediate',
#         category: 'restaurant'
#     },
#     response: {
#         success: true,
#         data: {
#             scenarios: [
#                 {
#                     id: 1,
#                     title: 'Ordering at a Restaurant',
#                     description: 'Practice ordering food and drinks',
#                     difficulty: 'intermediate',
#                     dialogue_count: 8
#                 }
#             ]
#         }
#     }
# };

# # // GET /conversation-craft/scenario/:id
# # // Get specific conversation scenario
# const getConversationScenario = {
#     method: 'GET',
#     url: '/conversation-craft/scenario/1',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     response: {
#         success: true,
#         data: {
#             id: 1,
#             title: 'Ordering at a Restaurant',
#             dialogue: [
#                 {
#                     speaker: 'waiter',
#                     text: '¿Qué le gustaría ordenar?',
#                     translation: 'What would you like to order?'
#                 },
#                 {
#                     speaker: 'user',
#                     text: '',
#                     options: [
#                         'Me gustaría una pizza, por favor.',
#                         'No sé qué quiero.',
#                         '¿Cuál es la especialidad de la casa?'
#                     ]
#                 }
#             ]
#         }
#     }
# };

# # // ==========================================
# # // PRONUNCIATION CRAFT ENDPOINTS
# # // ==========================================

# # // GET /pronunciation-craft/exercises
# # // Get pronunciation exercises
# const getPronunciationExercises = {
#     method: 'GET',
#     url: '/pronunciation-craft/exercises',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         language: 'spanish',
#         phoneme: 'rr'
#     }
# };

# # // POST /pronunciation-craft/analyze
# # // Submit audio for pronunciation analysis
# const analyzePronunciation = {
#     method: 'POST',
#     url: '/pronunciation-craft/analyze',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'multipart/form-data'
#     },
#     body: {
#         audio_file: 'audio_blob',
#         target_text: 'perro',
#         language: 'spanish'
#     },
#     response: {
#         success: true,
#         data: {
#             score: 85,
#             feedback: 'Good pronunciation of the double R sound',
#             phoneme_scores: {
#                 'p': 95,
#                 'e': 90,
#                 'rr': 75,
#                 'o': 90
#             }
#         }
#     }
# };

# # // ==========================================
# # // WORDS CRAFT ENDPOINTS
# # // ==========================================

# # // GET /words-craft/vocabulary
# # // Get vocabulary lists
# const getVocabulary = {
#     method: 'GET',
#     url: '/words-craft/vocabulary',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         language: 'spanish',
#         category: 'food',
#         level: 'beginner'
#     },
#     response: {
#         success: true,
#         data: {
#             vocabulary: [
#                 {
#                     id: 1,
#                     word: 'manzana',
#                     translation: 'apple',
#                     pronunciation: '/manˈθana/',
#                     example: 'Me gusta comer manzanas.',
#                     image_url: 'https://api.langcraft.com/images/apple.jpg'
#                 }
#             ]
#         }
#     }
# };

# # // POST /words-craft/quiz
# # // Start vocabulary quiz
# const startVocabularyQuiz = {
#     method: 'POST',
#     url: '/words-craft/quiz',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'application/json'
#     },
#     body: {
#         category: 'food',
#         level: 'beginner',
#         question_count: 10
#     }
# };

# # // POST /words-craft/quiz/answer
# # // Submit quiz answer
# const submitQuizAnswer = {
#     method: 'POST',
#     url: '/words-craft/quiz/answer',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'application/json'
#     },
#     body: {
#         quiz_id: 123,
#         question_id: 1,
#         answer: 'manzana',
#         time_taken: 5000 // milliseconds
#     }
# };

# # // ==========================================
# # // GRAMMAR CRAFT ENDPOINTS
# # // ==========================================

# # // GET /grammar-craft/rules
# # // Get grammar rules and lessons
# const getGrammarRules = {
#     method: 'GET',
#     url: '/grammar-craft/rules',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         language: 'spanish',
#         topic: 'verb_conjugation',
#         level: 'intermediate'
#     },
#     response: {
#         success: true,
#         data: {
#             rules: [
#                 {
#                     id: 1,
#                     title: 'Present Tense Conjugation',
#                     description: 'Learn how to conjugate regular verbs in present tense',
#                     examples: [
#                         {
#                             verb: 'hablar',
#                             conjugations: {
#                                 'yo': 'hablo',
#                                 'tú': 'hablas',
#                                 'él/ella': 'habla'
#                             }
#                         }
#                     ]
#                 }
#             ]
#         }
#     }
# };

# # // POST /grammar-craft/exercise
# # // Submit grammar exercise
# const submitGrammarExercise = {
#     method: 'POST',
#     url: '/grammar-craft/exercise',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here',
#         'Content-Type': 'application/json'
#     },
#     body: {
#         exercise_id: 1,
#         answers: [
#             {
#                 question_id: 1,
#                 answer: 'hablo'
#             },
#             {
#                 question_id: 2,
#                 answer: 'hablas'
#             }
#         ]
#     }
# };

# # // ==========================================
# # // PROGRESS AND ANALYTICS ENDPOINTS
# # // ==========================================

# # // GET /progress/overview
# # // Get user's overall progress
# const getProgressOverview = {
#     method: 'GET',
#     url: '/progress/overview',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     response: {
#         success: true,
#         data: {
#             total_lessons_completed: 45,
#             words_learned: 234,
#             current_streak: 5,
#             time_studied_minutes: 1250,
#             level: 'intermediate',
#             badges_earned: ['First Lesson', 'Word Master', '7-Day Streak'],
#             progress_by_skill: {
#                 idiom_craft: 75,
#                 conversation_craft: 60,
#                 pronunciation_craft: 45,
#                 words_craft: 80,
#                 grammar_craft: 55
#             }
#         }
#     }
# };

# # // GET /progress/statistics
# # // Get detailed learning statistics
# const getStatistics = {
#     method: 'GET',
#     url: '/progress/statistics',
#     headers: {
#         'Authorization': 'Bearer jwt_token_here'
#     },
#     params: {
#         period: 'week' // week, month, year
#     }
# };

# # // ==========================================
# # // UTILITY ENDPOINTS
# # // ==========================================

# # // GET /languages
# # // Get supported languages
# const getSupportedLanguages = {
#     method: 'GET',
#     url: '/languages',
#     response: {
#         success: true,
#         data: {
#             languages: [
#                 {
#                     code: 'es',
#                     name: 'Spanish',
#                     flag: '🇪🇸'
#                 },
#                 {
#                     code: 'fr',
#                     name: 'French',
#                     flag: '🇫🇷'
#                 },
#                 {
#                     code: 'de',
#                     name: 'German',
#                     flag: '🇩🇪'
#                 }
#             ]
#         }
#     }
# };

# # // Export all endpoints for documentation
# module.exports = {
#     # // Authentication
#     loginEndpoint,
#     registerEndpoint,
#     logoutEndpoint,
    
#     # // User Profile
#     getUserProfile,
#     updateUserProfile,
    
#     # // Idiom Craft
#     getIdiomLessons,
#     getIdiomLesson,
#     submitIdiomProgress,
    
#     # // Conversation Craft
#     getConversationScenarios,
#     getConversationScenario,
    
#     # // Pronunciation Craft
#     getPronunciationExercises,
#     analyzePronunciation,
    
#     # // Words Craft
#     getVocabulary,
#     startVocabularyQuiz,
#     submitQuizAnswer,
    
#     # // Grammar Craft
#     getGrammarRules,
#     submitGrammarExercise,
    
#     # // Progress
#     getProgressOverview,
#     getStatistics,
    
#     # // Utilities
#     getSupportedLanguages
# };
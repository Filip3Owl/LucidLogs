import logging
import random
import time

# Configuração básica
logging.basicConfig(filename='test_app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

actions = ["LOGIN_SUCCESS", "QUERY_VECTOR_DB", "EMBEDDING_GENERATED", "API_ERROR", "TOKEN_LIMIT_REACHED"]

# Gera 100 linhas de log para teste
for _ in range(100):
    action = random.choice(actions)
    level = "INFO" if "ERROR" not in action else "ERROR"
    logging.log(getattr(logging, level), f"User_123 executed {action}")
    time.sleep(0.01)
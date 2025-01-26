import pandas as pd
from config import CSV_FILE

def create_user_data_file():
    """Создает файл для хранения данных пользователей, если он не существует."""
    try:
        open(CSV_FILE, 'x').close()  # Попытка создать файл
        df = pd.DataFrame(columns=['user_id', 'username', 'first_name', 'last_name', 'registered', 'step', 'questionnaire_step'])
        df.to_csv(CSV_FILE, index=False) # Записываем колонки
    except FileExistsError:
        pass  # Файл уже существует

def add_user(user_id, username, first_name, last_name):
    """Добавляет пользователя в файл с данными."""
    df = pd.read_csv(CSV_FILE)
    if user_id not in df['user_id'].values:
        new_row = {'user_id': user_id, 'username': username, 'first_name': first_name, 'last_name': last_name, 'registered': True, 'step': None, 'questionnaire_step': None}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

def get_user(user_id):
    """Получает данные пользователя по user_id."""
    df = pd.read_csv(CSV_FILE)
    user_data = df[df['user_id'] == user_id]
    if not user_data.empty:
        return user_data.iloc[0].to_dict()
    return None

def update_user(user_id, data):
    """Обновляет данные пользователя."""
    df = pd.read_csv(CSV_FILE)
    df.loc[df['user_id'] == user_id, list(data.keys())] = list(data.values())
    df.to_csv(CSV_FILE, index=False)

def update_user_step(user_id, step):
    """Обновляет текущий шаг пользователя в FSM."""
    update_user(user_id, {'step': step})

def update_user_questionnaire_step(user_id, step):
    """Обновляет текущий шаг пользователя в FSM анкеты."""
    update_user(user_id, {'questionnaire_step': step})

def get_all_registered_users():
    """Получает список всех зарегистрированных пользователей."""
    df = pd.read_csv(CSV_FILE)
    registered_users = df[df['registered'] == True]
    return registered_users['user_id'].tolist()


def get_all_users():
    """Возвращает всех пользователей."""
    return pd.read_csv(CSV_FILE)


def add_user_feedback(user_id, feedback):
    """ Добавляет отзыв пользователя в файл с данными."""
    df = pd.read_csv(CSV_FILE)
    if "feedback" not in df.columns:
        df["feedback"] = None
    df.loc[df['user_id'] == user_id, 'feedback'] = feedback
    df.to_csv(CSV_FILE, index=False)
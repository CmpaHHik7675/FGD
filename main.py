from controllers import user_controller
from views import user_view

def main():
    # Пример создания и отображения пользователя
    user = user_controller.create_user("john_doe", "john@example.com")
    user_view.display_user(user)

if __name__ == '__main__':
    main()

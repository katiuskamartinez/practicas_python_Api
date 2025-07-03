import re
import getpass

def validacion_password():
  password_input = getpass.getpass("Inserte una contraseña segura: ")
  password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:'\"|,.<>/?]).{8,}$"

  if re.search(password_regex, password_input):
    print("La contraseña es segura.")
  else:
    print("La contraseña NO es segura.")

if __name__ == '__main__':
  validacion_password()
import allure


@allure.step
def print_encap(encap):
    return f'Encap: {encap}'

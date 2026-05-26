import pytest

@pytest.fixture(scope="function")
def todo_page(page):
    page.goto("https://demo.playwright.dev/todomvc")
    yield page

@pytest.fixture(scope="function")
def page_with_items(todo_page):
    items = ["Buy groceries", "Walk the dog", "Read a book"]
    for item in items:
        todo_page.locator(".new-todo").fill(item)
        todo_page.locator(".new-todo").press("Enter")
    return todo_page
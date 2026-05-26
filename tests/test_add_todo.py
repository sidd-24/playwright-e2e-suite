from playwright.sync_api import expect

def test_add_single_todo(todo_page):
    todo_page.locator(".new-todo").fill("Buy groceries")
    todo_page.locator(".new-todo").press("Enter")
    expect(todo_page.locator(".todo-list li")).to_have_count(1)
    expect(todo_page.locator(".todo-list li")).to_contain_text("Buy groceries")

def test_add_multiple_todos(todo_page):
    items = ["Task one", "Task two", "Task three"]
    for item in items:
        todo_page.locator(".new-todo").fill(item)
        todo_page.locator(".new-todo").press("Enter")
    expect(todo_page.locator(".todo-list li")).to_have_count(3)

def test_empty_input_does_not_add_todo(todo_page):
    todo_page.locator(".new-todo").press("Enter")
    expect(todo_page.locator(".todo-list li")).to_have_count(0)
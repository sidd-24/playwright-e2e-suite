from playwright.sync_api import expect

def test_delete_a_todo(page_with_items):
    first_item = page_with_items.locator(".todo-list li").first
    first_item.hover()
    first_item.locator(".destroy").click()
    expect(page_with_items.locator(".todo-list li")).to_have_count(2)

def test_delete_all_todos(page_with_items):
    items = page_with_items.locator(".todo-list li")
    count = items.count()
    for i in range(count):
        item = page_with_items.locator(".todo-list li").first
        item.hover()
        item.locator(".destroy").click()
    expect(page_with_items.locator(".todo-list li")).to_have_count(0)
from playwright.sync_api import expect

def test_complete_a_todo(page_with_items):
    page_with_items.locator(".todo-list li").first.locator(".toggle").click()
    expect(page_with_items.locator(".todo-list li").first).to_have_class("completed")

def test_completed_count_updates(page_with_items):
    page_with_items.locator(".todo-list li").first.locator(".toggle").click()
    expect(page_with_items.locator(".todo-count")).to_contain_text("2 items left")
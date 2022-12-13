from unittest import TestCase
from django.urls import resolve

from myapp.views import top,myapp_new,myapp_edit,myapp_detail

# Create your tests here.
class TopPageTest(TestCase):
  def test_top_page_returns_200_and_expected_title(self):
    response = self.client.get("/")
    self.assertContains(response,"Django",status_code=200)
  def test_top_page_uses_expected_template(self):
    response = self.client.get("/")
    self.assertTemplateUsed(response,"myapp/top.html")
    
class CreateMyappTest(TestCase):
  def test_should_resolve_myapp_new(self):
    found = resolve("/myapp/new/")
    self.assertEqual(myapp_new,found.func)
    
class MyappDetailTest(TestCase):
  def test_should_resolve_myapp_detail(self):
    found = resolve("/myapp/I/")
    self.assertEqual(myapp_detail,found.func)
    
class EditMyappTest(TestCase):
  def test_should_resolve_myapp_edit(self):
    found = resolve("/myapp/I/edit/")
    self.assertEqual(myapp_edit,found.func)



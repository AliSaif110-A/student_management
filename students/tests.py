from django.test import TestCase
from django.urls import reverse
from .models import Student

# Create your tests here.


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name="Ali", last_name="Saif", email="alisaif@nci.com")

    def test_student_model(self):
        self.assertEqual(self.student.first_name, "Ali")
        self.assertEqual(self.student.last_name, "Saif")
        self.assertEqual(self.student.email, "alisaif@nci.com")


class StudentListViewTest(TestCase):
    def test_student_list_view(self):
        url = reverse("students:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list.html")


class StudentSearchViewTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name="Ali", last_name="Saif", email="alisaif@nci.com")

    def test_student_search_view(self):
        url = reverse("students:search")
        response = self.client.get(url, {"query": "Ali"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ali")


class StudentEditViewTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name="Ali", last_name="Saif", email="alisaif@nci.com")

    def test_student_edit_view(self):
        data = {"first_name": "Abhishek", "last_name": "Malik", "email": "AbhishekMalik@nci.com"}
        url = reverse("students:update", kwargs={"pk": self.student.pk})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, "Abhishek")
        self.assertEqual(self.student.last_name, "Malik")
        self.assertEqual(self.student.email, "AbhishekMalik@nci.com")


class StudentDeleteViewTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name="Ali", last_name="Saif", email="alisaif@nci.com")

    def test_student_delete_view(self):
        url = reverse("students:delete", kwargs={"pk": self.student.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
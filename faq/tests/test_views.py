import pytest
from django.test import Client
from faq.models import FAQ
from django.urls import reverse


@pytest.mark.django_db
def test_faq_list():
    # Create a FAQ object with a question and an answer
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")

    # Ensure the FAQ has been saved with the correct translations
    assert faq.question == "What is Django?"
    assert faq.answer == "A web framework."

    # Use Django's test client to simulate a GET request
    client = Client()

    # Make a GET request to the API with the lang=hi query parameter (for Hindi translation)
    response = client.get(reverse("faq-list") + "?lang=hi")

    # Ensure the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the translated question (in Hindi) exists in the response data
    # Assuming the translation for "What is Django?" to Hindi is returned as "Django क्या है?"
    translated_question = "Django क्या है?"
    assert any(
        faq_item["question"] == translated_question for faq_item in response.json()
    )

    assert any(faq_item["answer"] == "A web framework." for faq_item in response.json())

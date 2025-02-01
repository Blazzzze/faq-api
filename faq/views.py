from rest_framework import viewsets
from rest_framework.response import Response
from faq.models import FAQ
from faq.serializers import FAQSerializer


class FAQViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing FAQ instances.

    This view set provides actions to list, create, retrieve, update, and delete FAQ objects.
    It customizes the `list` method to include translated questions based on the specified language.
    """

    # Retrieve all FAQ objects from the database
    queryset = FAQ.objects.all()

    # Use the FAQSerializer for serializing the FAQ objects
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """
        Custom list action that retrieves all FAQs and returns the questions translated
        into the specified language.

        The language is provided via the 'lang' query parameter (default is "en").

        Args:
            request: The HTTP request object containing the query parameters.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response containing the list of FAQs with translated questions.
        """

        lang = request.GET.get("lang", "en")
        faqs = self.get_queryset()

        # Prepare the data with the translated questions based on the language
        data = [
            {
                "id": faq.id,
                "question": faq.get_translated_question(lang),  # Translated question
                "answer": faq.answer,  # The answer remains the same
            }
            for faq in faqs
        ]

        return Response(data)

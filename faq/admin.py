from django.contrib import admin
from faq.models import FAQ
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class FAQAdminForm(forms.ModelForm):
    """
    Custom form for FAQ Admin with CKEditor support.

    This form provides a rich text editor for the FAQ answers using the CKEditor widget.
    """

    answer = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        """
        Meta class for the FAQAdminForm.

        Attributes:
            model (FAQ): The FAQ model that this form is associated with.
            fields (str): The fields that are included in this form. In this case, all fields are included.
        """

        model = FAQ
        fields = "__all__"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    FAQ Admin Interface

    This class provides the admin interface for managing FAQs in the Django application.
    It includes a custom form with a rich text editor for the FAQ answers.
    """

    # The custom form that is used for this admin interface.
    form = FAQAdminForm

    # The fields that are displayed in the admin list view.
    list_display = (
        "question",
        "question_hi",
        "question_bn",
        "short_answer",
        "created_at",
    )

    # The fields that are searchable in the admin interface.
    search_fields = ("question", "question_hi", "question_bn")

    # The fields that are filterable in the admin interface.
    list_filter = ("question",)

    # The fields that are read-only in the admin interface.
    readonly_fields = ("created_at", "updated_at")

    def short_answer(self, obj):
        """
        A custom method that returns a shortened version of the FAQ answer.

        Args:
            obj (FAQ): The FAQ object that this method is called on.

        Returns:
            str: A shortened version of the FAQ answer.
        """
        return obj.answer[:50] + "..." if len(obj.answer) > 50 else obj.answer

    # The short description that is displayed for this custom method in the admin interface.
    short_answer.short_description = "Short Answer"

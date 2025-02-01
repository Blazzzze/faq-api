from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from faq.services import translate_text, get_cached_translation


class FAQ(models.Model):
    # Field to store the question in the default language
    question = models.TextField(verbose_name=_("Question"))

    # Field to store the answer in rich text format
    answer = RichTextField(verbose_name=_("Answer"))

    # Field to store the question translation in Hindi (optional)
    question_hi = models.TextField(
        verbose_name=_("Question in Hindi"), blank=True, null=True
    )

    # Field to store the question translation in Bengali (optional)
    question_bn = models.TextField(
        verbose_name=_("Question in Bengali"), blank=True, null=True
    )

    def get_translated_question(self, lang):
        """
        Retrieves the translation of the question in the specified language.

        Args:
            lang (str): The language code (e.g., 'hi' for Hindi, 'bn' for Bengali).

        Returns:
            str: The translated question text.
        """
        return get_cached_translation(self, lang)

    def save(self, *args, **kwargs):
        """
        Automatically translates the question into Hindi and Bengali if translations
        are not provided, before saving the FAQ object.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        This method ensures that the question is always translated into Hindi and
        Bengali if the translations aren't already set.
        """
        # Automatically translate the question to Hindi if not provided
        if not self.question_hi and self.question:
            cached_hi = get_cached_translation(self, "hi")
            self.question_hi = (
                cached_hi if cached_hi else translate_text(self.question, "hi")
            )

        # Automatically translate the question to Bengali if not provided
        if not self.question_bn and self.question:
            cached_bn = get_cached_translation(self, "bn")
            self.question_bn = (
                cached_bn if cached_bn else translate_text(self.question, "bn")
            )

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the FAQ object, which is the question.

        Returns:
            str: The question text.
        """
        return self.question

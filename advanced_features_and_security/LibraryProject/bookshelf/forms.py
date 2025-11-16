# bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Search books..."})
    )

    def clean_q(self):
        q = self.cleaned_data.get("q", "")
        # Additional validation/sanitization if needed:
        # e.g. strip control characters:
        return q.strip()

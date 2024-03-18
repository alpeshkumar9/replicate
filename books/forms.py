from django import forms


class BookLoanAdminForm(forms.ModelForm):
    """
    Custom admin form for BookLoan to display user's full name in the dropdown.
    """

    def __init__(self, *args, **kwargs):
        super(BookLoanAdminForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f"{obj.get_full_name()} ({obj.username})"

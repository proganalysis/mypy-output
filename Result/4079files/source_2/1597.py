from show_off_web_app.viewmodels.signin_viewmodel import SigninViewModel


class RegisterViewModel(SigninViewModel):
    def __init__(self):
        super().__init__()
        self.confirm_password = None

    def from_dict(self, data_dict):
        super().from_dict(data_dict)
        self.confirm_password = data_dict.get('confirm_password')

    def validate(self):
        self.error = None
        if self.password != self.confirm_password:
            self.error = "The password and confirmation don't match"
            return

        if not self.password:
            self.error = "You must specify a password"
            return

        if not self.email:
            self.error = "You must specify an email address"
            return

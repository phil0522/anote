package aaron.org.anote.login;

public class LoginViewModelImpl implements LoginViewModel {
    private LoginModel model;

    public LoginViewModelImpl(LoginModel model) {
        this.model = model;
    }

    @Override
    public String getUserName() {
        return model.getUserName();
    }

    @Override
    public String getPassword() {
        return model.getPassword();
    }

    @Override
    public void onUserNameChanged(String text) {
        model.setUserName(text);
    }

    @Override
    public void onPasswordChanged(String text) {
        model.setPassword(text);
    }
}

package aaron.org.anote.login;

import org.aaron.plugin.OnTextChange;

import aaron.org.anote.viewbinder.ViewModel;

public interface LoginViewModel extends ViewModel {
    String getUserName();


    String getPassword();

    @OnTextChange
    void onUserNameChanged(String text);

    @OnTextChange
    void onPasswordChanged(String text);
}

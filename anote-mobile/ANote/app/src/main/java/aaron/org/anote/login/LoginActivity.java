package aaron.org.anote.login;

import android.os.Bundle;

import aaron.org.anote.viewbinder.DynamicActivity;

public class LoginActivity extends DynamicActivity {
    LoginModel loginModel = new LoginModel("User", "Pass");
    LoginViewModelImpl loginViewModel = new LoginViewModelImpl(loginModel);

    @Override
    public void onCreate(Bundle savedInstance) {
        super.onCreate(savedInstance);

        setContentView(LoginLayout.create(loginViewModel).getView());
    }
}

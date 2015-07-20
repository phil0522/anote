package aaron.org.anote.login;

import android.text.Editable;
import android.text.TextWatcher;

import aaron.org.anote.viewbinder.ObservableStringField;

public class LoginViewModelWrapper2 {
    private final LoginViewModel viewModel;
    public LoginViewModelWrapper2(LoginViewModel viewModel) {
        this.viewModel = viewModel;
    }

    public ObservableStringField getUserName() {
        return new ObservableStringField() {
            @Override
            public String getValue() {
                return viewModel.getUserName();
            }
        };
    }

    public ObservableStringField getPassword() {
        return new ObservableStringField() {
            @Override
            public String getValue() {
                return viewModel.getPassword();
            }
        };
    }

    public TextWatcher onUserNameChanged() {
        return new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                viewModel.onUserNameChanged(s.toString());
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        };
    }

    public TextWatcher onPasswordChanged() {
        return new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                viewModel.onPasswordChanged(s.toString());
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        };
    }
}

package aaron.org.anote.login;

import android.view.ViewGroup.LayoutParams;
import android.widget.LinearLayout;

import aaron.org.anote.viewbinder.Layout;
import aaron.org.anote.viewbinder.ViewNode;

public class LoginLayout extends Layout<LoginViewModel> {
    public static ViewNode create(LoginViewModel viewModel) {
        LoginViewModelWrapper2 proxy = new LoginViewModelWrapper2(viewModel);
        return linearLayout(
                orientation(LinearLayout.VERTICAL),
                layoutWidth(LayoutParams.MATCH_PARENT),
                layoutHeight(LayoutParams.WRAP_CONTENT),
                textView(text(proxy.getUserName())),
                textView(text("vvvvvvvvvvvvvvv")),
                textView(text(proxy.getPassword())),
                onClick(proxy.onPasswordChanged())
        );
    }

    @Override
    public void refresh(LoginViewModel viewModel) {

    }
}

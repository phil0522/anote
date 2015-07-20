package aaron.org.anote.viewbinder;

import android.text.Editable;
import android.text.TextWatcher;

/**
 * Created by phil on 2015/6/30.
 */
public class TextChangeListener implements TextWatcher {
    @Override
    public void beforeTextChanged(CharSequence s, int start, int count, int after) {

    }

    @Override
    public void onTextChanged(CharSequence s, int start, int before, int count) {
        onTextChanged(s.toString());
    }

    @Override
    public void afterTextChanged(Editable s) {

    }

    public void onTextChanged(String s) {
        throw new UnsupportedOperationException("Stub");
    }
}

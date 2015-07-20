package aaron.org.anote.viewbinder;

import android.app.Activity;
import android.os.Bundle;

public class DynamicActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstance) {
        super.onCreate(savedInstance);
        Layout.start(this);
    }
}

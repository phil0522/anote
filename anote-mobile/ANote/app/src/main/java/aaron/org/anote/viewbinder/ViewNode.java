package aaron.org.anote.viewbinder;

import android.view.View;

public class ViewNode implements Node {
    private View view;

    public ViewNode (View view) {
        this.view = view;
    }
    public View getView() {
        return view;
    }
}

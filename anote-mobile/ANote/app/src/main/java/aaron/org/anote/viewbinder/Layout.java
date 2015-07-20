package aaron.org.anote.viewbinder;

import android.content.Context;
import android.text.TextWatcher;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.lang.ref.WeakReference;

import aaron.org.anote.viewbinder.PropertyNode.ViewProperty;

public abstract class Layout<T extends ViewModel> {
    public abstract void refresh(T viewModel);

    private static WeakReference<Context> mContext;
    public static void start(Context activityContext) {
        mContext = new WeakReference<>(activityContext);
    }

    public static Context getContext() {
        if (mContext.get() == null) {
            throw new UnsupportedOperationException("context has been cleared.");
        }
        return mContext.get();
    }

    private static void applyArgs(View view, Node... nodes) {
        ViewGroup viewGroup = null;
        if (view instanceof ViewGroup) {
            viewGroup = (ViewGroup) view;
        }
        for (Node node : nodes) {
            if (node instanceof ViewNode) {
                if (viewGroup != null) {
                    ViewNode viewNode = (ViewNode) node;
                    viewGroup.addView(viewNode.getView());
                } else {
                    throw new UnsupportedOperationException(String.format(
                            "View %s can't have child view", view.toString()));
                }
            } else if (node instanceof PropertyNode) {
                PropertyNode propertyNode = (PropertyNode) node;
                propertyNode.applyProperty(view);
            }
        }
    }

    public static ViewNode linearLayout(Node... nodes) {
        LinearLayout layout = new LinearLayout(getContext());
        applyArgs(layout, nodes);
        return new ViewNode(layout);
    }

    public static ViewNode frameLayout(Node... nodes) {
        FrameLayout layout = new FrameLayout(getContext());
        applyArgs(layout, nodes);
        return new ViewNode(layout);
    }

    public static ViewNode textView(PropertyNode... nodes) {
        TextView textView = new TextView(getContext());
        applyArgs(textView, nodes);
        return new ViewNode(textView);
    }

    public static PropertyNode orientation(Integer direction) {
        return new PropertyNode(ViewProperty.ORIENTATION, direction);
    }

    public static PropertyNode layoutWidth(Integer size) {
        return new PropertyNode(ViewProperty.LAYOUT_WIDTH, size);
    }

    public static PropertyNode layoutHeight(Integer size) {
        return new PropertyNode(ViewProperty.LAYOUT_HEIGHT, size);
    }

    public static PropertyNode text(String text) {
        return new PropertyNode(ViewProperty.TEXT, text);
    }

    public static PropertyNode text(ObservableStringField text) {
        return new PropertyNode(ViewProperty.TEXT, text);
    }

    public static PropertyNode onClick(TextWatcher watcher) {
        return new PropertyNode(ViewProperty.ON_CLICK, watcher);
    }
}

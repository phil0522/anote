package aaron.org.anote.viewbinder;

import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnLongClickListener;
import android.view.ViewGroup.MarginLayoutParams;
import android.widget.Checkable;
import android.widget.LinearLayout;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.lang.reflect.Proxy;

import aaron.org.anote.viewbinder.proxy.ProxiedObject;

public class PropertyNode implements Node {
    private static final String LOG_TAG = PropertyNode.class.getCanonicalName();
    public enum ViewProperty {
        BACKGROUND,
        BACKGROUND_COLOR,
        CHECKED,
        CLICKABLE,
        ENABLED,
        FOCUSABLE,
        HINT,
        ID,
        INPUT_TYPE,
        LAYOUT_HEIGHT,
        LAYOUT_MARGIN,
        LAYOUT_MARGIN_BOTTOM,
        LAYOUT_MARGIN_END,
        LAYOUT_MARGIN_START,
        LAYOUT_MARGIN_TOP,
        LAYOUT_WEIGHT,
        LAYOUT_WIDTH,
        LIST_ADAPTER,
        ON_CLICK,
        ON_LONG_CLICK,
        ON_TEXT_CHANGED,
        ORIENTATION,
        PADDING,
        PADDING_BOTTOM,
        PADDING_LEFT,
        PADDING_RIGHT,
        PADDING_TOP,
        SCROLLBARS,
        SINGLE_LINE,
        TEXT,
        TEXT_ALIGNMENT,
        TEXT_APPEARANCE,
        TEXT_COLOR,
        TEXT_COLOR_HINT,
        TEXT_COLOR_LINK,
        TEXT_IS_SELECTABLE,
        TEXT_SIZE,
        VISIBILITY,
    }

    private ViewProperty property;
    private Object value;
    public PropertyNode(ViewProperty property, Object value) {
        this.property = property;
        this.value = value;
    }

    public boolean applyProperty(final View view) {
        switch (property) {
            case BACKGROUND:
                if (value == null) {
                    view.setBackgroundResource(0);
                    return true;
                } else if (value instanceof Integer) {
                    view.setBackgroundResource((Integer)value);
                    return true;
                }
                break;
            case BACKGROUND_COLOR:
                if (value == null) {
                    view.setBackgroundResource(0);
                    return true;
                } else if (value instanceof Integer) {
                    view.setBackgroundColor((Integer)value);
                    return true;
                }
                break;
            case CHECKED:
                ((Checkable) view).setChecked((Boolean) value);
                return true;
            case CLICKABLE:
                view.setClickable((Boolean) value);
                return true;
            case ENABLED:
                view.setEnabled((Boolean) value);
                return true;
            case FOCUSABLE:
                view.setEnabled((Boolean) value);
                return true;
            case HINT:
                if (value instanceof String) {
                    ((TextView) view).setHint((String) value);
                    return true;
                } else if (value instanceof Integer) {
                    ((TextView) view).setHint(value.toString());
                    return true;
                }
                break;
            case ID:
                view.setId((Integer) value);
                return true;
            case INPUT_TYPE:
                ((TextView) view).setRawInputType((Integer) value);
                return true;
            case LAYOUT_HEIGHT:
                if (view.getLayoutParams() != null) {
                    view.getLayoutParams().height = (Integer) value;
                    view.requestLayout();
                }
                return true;
            case LAYOUT_MARGIN:
                if (view.getLayoutParams() instanceof MarginLayoutParams) {
                    MarginLayoutParams lp = (MarginLayoutParams) view.getLayoutParams();
                    int val = (Integer) value;
                    lp.setMargins(val, val, val, val);
                    view.requestLayout();
                    return true;
                }
                break;
            case LAYOUT_MARGIN_BOTTOM:
                if (view.getLayoutParams() instanceof MarginLayoutParams) {
                    MarginLayoutParams lp = (MarginLayoutParams) view.getLayoutParams();
                    lp.bottomMargin = (Integer) value;
                    view.requestLayout();
                    return true;
                }
                break;
            case LAYOUT_MARGIN_END:
                if (view.getLayoutParams() instanceof MarginLayoutParams) {
                    MarginLayoutParams lp = (MarginLayoutParams) view.getLayoutParams();
                    lp.setMarginEnd((Integer) value);
                    view.requestLayout();
                    return true;
                }
                break;
            case LAYOUT_MARGIN_START:
                if (view.getLayoutParams() instanceof MarginLayoutParams) {
                    MarginLayoutParams lp = (MarginLayoutParams) view.getLayoutParams();
                    lp.setMarginStart((Integer) value);
                    view.requestLayout();
                    return true;
                }
                break;
            case LAYOUT_MARGIN_TOP:
                if (view.getLayoutParams() instanceof MarginLayoutParams) {
                    MarginLayoutParams lp = (MarginLayoutParams) view.getLayoutParams();
                    lp.topMargin = (Integer) value;
                    view.requestLayout();
                    return true;
                }
                break;
            case LAYOUT_WEIGHT:
                if (view.getLayoutParams() != null) {
                    if (view.getLayoutParams() instanceof LinearLayout.LayoutParams) {
                        ((LinearLayout.LayoutParams) view.getLayoutParams()).weight = (Float) value;
                        view.requestLayout();
                    } else {
                        Log.w(LOG_TAG, "Can't apply layout_weight to " + view);
                    }
                }
                return true;
            case LAYOUT_WIDTH:
                if (view.getLayoutParams() != null) {
                    view.getLayoutParams().width = (Integer) value;
                    view.requestLayout();
                }
                return true;
            case LIST_ADAPTER:
                if (value instanceof ListAdapter) {
                    if (view instanceof ListView) {
                        ((ListView) view).setAdapter((ListAdapter)value);
                        return true;
                    }
                }
            case ON_CLICK:
                if (value == null) {
                    view.setOnClickListener(null);
                    return true;
                } else if (value instanceof ProxiedObject) {
                    view.setOnClickListener(new OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            ViewModel viewModel = ViewModelManager.getViewModel(view);
                            if (viewModel != null) {
                                DynamicLayoutInnovationHandler handler = (DynamicLayoutInnovationHandler)
                                        Proxy.getInvocationHandler(value);


                            }
                        }
                    });
                    return true;
                }
                break;
            case ON_LONG_CLICK:
                if (value == null) {
                    view.setOnClickListener(null);
                    return true;
                } else if (value instanceof OnLongClickListener) {
                    view.setOnLongClickListener((OnLongClickListener) value);
                    return true;
                }
                break;
            case ON_TEXT_CHANGED:
                if (view instanceof TextView) {
                    ((TextView) view).addTextChangedListener((TextWatcher) value);
                    return true;
                }
                break;
            case ORIENTATION:
                if (view instanceof LinearLayout) {
                    ((LinearLayout) view).setOrientation((Integer) value);
                    return true;
                }
                break;
            case PADDING:
                if (value instanceof Integer) {
                    int val = (Integer) value;
                    view.setPadding(val, val, val, val);
                    return true;
                }
                break;
            case PADDING_BOTTOM:
                view.setPadding(
                        view.getPaddingLeft(),
                        view.getPaddingTop(),
                        view.getPaddingRight(),
                        (Integer) value);
                return true;
            case PADDING_LEFT:
                view.setPadding(
                        (Integer) value,
                        view.getPaddingTop(),
                        view.getPaddingRight(),
                        view.getPaddingBottom());
                return true;
            case PADDING_RIGHT:
                view.setPadding(
                        view.getPaddingLeft(),
                        view.getPaddingTop(),
                        (Integer) value,
                        view.getPaddingBottom());
                return true;
            case PADDING_TOP:
                view.setPadding(
                        view.getPaddingLeft(),
                        (Integer) value,
                        view.getPaddingRight(),
                        view.getPaddingBottom());
                return true;
            case SCROLLBARS:
                view.setHorizontalScrollBarEnabled((Boolean) value);
                view.setVerticalScrollBarEnabled((Boolean) value);
                return true;
            case SINGLE_LINE:
                ((TextView) view).setSingleLine((Boolean) value);
                return true;
            case TEXT:
                if (value instanceof  String) {
                    ((TextView) view).setText((String) value);
                    return true;
                } else if (value instanceof ObservableStringField) {
                    ((TextView) view).setText(((ObservableStringField)value).getValue());
                    view.setTag(0, value);
                    return true;
                }
                break;
            case TEXT_ALIGNMENT:
                view.setTextAlignment((Integer) value);
                return true;
            case TEXT_APPEARANCE:
                ((TextView) view).setTextAppearance(view.getContext(), (Integer) value);
                return true;
            case TEXT_COLOR:
                ((TextView) view).setTextColor((Integer) value);
                return true;
            case TEXT_COLOR_HINT:
                ((TextView) view).setHintTextColor((Integer) value);
                return true;
            case TEXT_COLOR_LINK:
                ((TextView) view).setLinkTextColor((Integer) value);
                return true;
            case TEXT_IS_SELECTABLE:
                ((TextView) view).setTextIsSelectable((Boolean) value);
                return true;
            case TEXT_SIZE:
                ((TextView) view).setTextSize(((Number)value).floatValue());
                return true;
            case VISIBILITY:
                view.setVisibility((Integer) value);
                return true;
        }

        // Either property not supported or value type is not accepted by the property.
        return false;
    }
}


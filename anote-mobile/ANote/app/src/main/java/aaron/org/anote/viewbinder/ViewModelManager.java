package aaron.org.anote.viewbinder;

import android.view.View;

import com.google.common.collect.LinkedListMultimap;
import com.google.common.collect.ListMultimap;

import java.lang.ref.WeakReference;
import java.util.List;

import aaron.org.anote.R;

public class ViewModelManager {
    private static ListMultimap<ViewModel, WeakReference<ViewNode>> nodeMap =
            LinkedListMultimap.create();

    public static void put(ViewModel viewModel, ViewNode node) {
        nodeMap.put(viewModel, new WeakReference<>(node));
        node.getView().setTag(R.id.view_model, viewModel);
    }

    public static void refreshView(ViewModel viewModel) {
        if (nodeMap.containsKey(viewModel)) {
            List<WeakReference<ViewNode>> nodes = nodeMap.get(viewModel);
            for (WeakReference<ViewNode> node : nodes) {
                if (node.get() == null) {
                    nodes.remove(node);
                }

            }
        }
    }

    public static ViewModel getViewModel(View view) {
        return (ViewModel) view.getTag(R.id.view_model);
    }
}

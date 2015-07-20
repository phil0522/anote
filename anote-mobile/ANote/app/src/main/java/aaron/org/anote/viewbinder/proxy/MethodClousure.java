package aaron.org.anote.viewbinder.proxy;

import java.lang.reflect.Method;

/**
 * A method object with all its arguments.
 */
public class MethodClousure<T> {
    Method method;
    Object[] args;

    public MethodClousure(Method method, Object[] args) {
        this.method = method;
        this.args = args;
    }
}

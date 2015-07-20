package org.aaron.plugin;

import org.apache.velocity.VelocityContext;
import org.apache.velocity.runtime.RuntimeConstants;
import org.apache.velocity.runtime.RuntimeInstance;
import org.apache.velocity.runtime.log.NullLogChute;
import org.apache.velocity.runtime.parser.ParseException;
import org.apache.velocity.runtime.parser.node.SimpleNode;
import org.apache.velocity.runtime.resource.ResourceCacheImpl;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import javax.lang.model.element.Element;

@SuppressWarnings("unused")  // the fields in this class are only read via reflection
public class ViewModelTemplateVars {
    String pkg;

    String name;

    String generatedClassName;

    Set<String> imports = new HashSet<>();

    List<MetaMethod> fields = new ArrayList<>();

    List<String> textChanges = new ArrayList<>();

    Element originatedElement;

    private static final RuntimeInstance velocityRuntimeInstance = new RuntimeInstance();

    static {
        velocityRuntimeInstance.setProperty(RuntimeConstants.RUNTIME_REFERENCES_STRICT, "true");
        velocityRuntimeInstance.setProperty(RuntimeConstants.RUNTIME_LOG_LOGSYSTEM_CLASS,
                new NullLogChute());
        velocityRuntimeInstance.setProperty(RuntimeConstants.RESOURCE_MANAGER_CACHE_CLASS,
                ResourceCacheImpl.class.getName());
        try {
            velocityRuntimeInstance.init();
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    ViewModelTemplateVars() {

    }

    static SimpleNode parsedTemplateForResource(String resourceName) {
        InputStream in = ViewModelTemplateVars.class.getResourceAsStream(resourceName);
        if (in == null) {
            throw new IllegalArgumentException("Could not find resource: " + resourceName);
        }
        try {
            Reader reader = new InputStreamReader(in, "UTF-8");
            return velocityRuntimeInstance.parse(reader, resourceName);
        } catch (UnsupportedEncodingException | ParseException e) {
            throw new AssertionError(e);
        }
    }

    void toText(Writer writer) {
        SimpleNode node = ViewModelTemplateVars.parsedTemplateForResource("/ViewModelWrapper.txt");
        VelocityContext velocityContext = new VelocityContext();
        imports.add("org.aaron.plugin.OnTextChange");
        velocityContext.put("pkg", pkg);
        velocityContext.put("name", name);
        velocityContext.put("generatedClassName", generatedClassName);
        velocityContext.put("fields", fields);
        velocityContext.put("imports", imports);
        velocityContext.put("textChanges", textChanges);
        velocityRuntimeInstance.render(velocityContext, writer, node.getTemplateName(), node);
    }
}

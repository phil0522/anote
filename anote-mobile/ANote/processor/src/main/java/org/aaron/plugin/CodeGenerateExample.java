package org.aaron.plugin;

import com.google.common.collect.ImmutableSet;

import java.io.IOException;
import java.io.Writer;
import java.util.HashMap;
import java.util.Set;

import javax.annotation.processing.AbstractProcessor;
import javax.annotation.processing.RoundEnvironment;
import javax.annotation.processing.SupportedSourceVersion;
import javax.lang.model.SourceVersion;
import javax.lang.model.element.Element;
import javax.lang.model.element.ExecutableElement;
import javax.lang.model.element.PackageElement;
import javax.lang.model.element.TypeElement;
import javax.tools.Diagnostic;
import javax.tools.Diagnostic.Kind;
import javax.tools.JavaFileObject;

@SupportedSourceVersion(SourceVersion.RELEASE_7)
public class CodeGenerateExample extends AbstractProcessor {
    private HashMap<String, ViewModelTemplateVars> viewModelTemplateVars;
    @Override
    public Set<String> getSupportedAnnotationTypes() {
        return ImmutableSet.of(
                Observable.class.getCanonicalName(),
                OnTextChange.class.getCanonicalName()
        );
    }

    @Override
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv) {
        viewModelTemplateVars = new HashMap<>();
        for (Element elem : roundEnv.getElementsAnnotatedWith(OnTextChange.class)) {
            String className = elem.getEnclosingElement().getSimpleName().toString();
            String packageName = packageNameOf((TypeElement) elem.getEnclosingElement());

            ViewModelTemplateVars templateVars = getOrCreateViewModelTemplate(packageName, className);

            templateVars.textChanges.add(elem.getSimpleName().toString());
            templateVars.imports.add("android.text.TextWatcher");
            templateVars.imports.add("android.text.Editable");
            processingEnv.getMessager().printMessage(Kind.WARNING, String.format(
                    "className: %s, packageName: %s : ele name: %s",
                    className, packageName, elem.getSimpleName()
            ));
        }

        for (Element elem : roundEnv.getElementsAnnotatedWith(Observable.class)) {
            String className = elem.getEnclosingElement().getSimpleName().toString();
            String packageName = packageNameOf((TypeElement) elem.getEnclosingElement());

            ViewModelTemplateVars templateVars = getOrCreateViewModelTemplate(packageName, className);

            ExecutableElement executableElement = (ExecutableElement) elem;
            templateVars.originatedElement = elem;
            templateVars.imports.add(Observable.class.getCanonicalName());
            templateVars.fields.add(
                    new MetaMethod(elem.getSimpleName().toString(),
                            executableElement.getReturnType().toString()));
            processingEnv.getMessager().printMessage(Kind.WARNING, String.format(
                    "className: %s, packageName: %s : ele name: %s",
                    className, packageName, elem.getSimpleName()
            ));
        }

        for (ViewModelTemplateVars var : viewModelTemplateVars.values()) {
            processingEnv.getMessager().printMessage(Kind.WARNING, String.format(
                "write new source: %s", var.generatedClassName
            ));
            writeSourceFile(var);
        }

        return true; // no further processing of this annotation type
    }

    static String packageNameOf(TypeElement type) {
        while (true) {
            Element enclosing = type.getEnclosingElement();
            if (enclosing instanceof PackageElement) {
                return ((PackageElement) enclosing).getQualifiedName().toString();
            }
            type = (TypeElement) enclosing;
        }
    }

    private ViewModelTemplateVars getOrCreateViewModelTemplate(String packageName, String className) {
        String fullName = packageName + "." + className;
        if (!viewModelTemplateVars.containsKey(fullName)) {
            ViewModelTemplateVars vars = new ViewModelTemplateVars();
            vars.pkg = packageName;
            vars.name = className;
            vars.generatedClassName = className + "Wrapper";
            viewModelTemplateVars.put(fullName, vars);
        }
        return viewModelTemplateVars.get(fullName);
    }

    private void writeSourceFile(ViewModelTemplateVars vars) {
        try {
            JavaFileObject sourceFile =
                    processingEnv.getFiler().createSourceFile(vars.pkg + '.' + vars.generatedClassName, vars.originatedElement);
            try (Writer writer = sourceFile.openWriter()) {
                vars.toText(writer);
            }
        } catch (IOException e) {
            processingEnv.getMessager().printMessage(Diagnostic.Kind.ERROR,
                    "Could not write generated class " + vars.name + ": " + e);
        }
    }


}

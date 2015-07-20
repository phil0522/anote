package org.aaron.plugin;

public class MetaMethod {
    private String name;
    private String type;
    public MetaMethod(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }
}

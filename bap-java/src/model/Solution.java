package model;

public abstract class Solution implements Comparable<Solution> {

    /**
     * Export solution to file.
     *
     * @param fileName file store name.
     */
    public abstract void exportToFile(String fileName);

    /**
     * Override equals method to check two solution objects whether are same.
     */
    @Override
    public abstract boolean equals(Object obj);

    /**
     * Override toString method for print convenient.
     */
    @Override
    public abstract String toString();

    /**
     * Override compareTo method to compare two solutions in the solution pool.
     */
    @Override
    public abstract int compareTo(Solution solution);

}

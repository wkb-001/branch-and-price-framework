package algorithm.branchandprice;

public record Arc(int From, int to) {

    @Override
    public String toString() {
        return "Branch Arc = (" + From + ", " + to + ')';
    }

}

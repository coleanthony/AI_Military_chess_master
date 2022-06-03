'''
Store piece move in alpha beta search.
'''

'''
public class AlphaBetaNode {
    public String piece;
    public int[] from;
    public int[] to;
    public int value;

    public AlphaBetaNode(String piece, int[] from, int[] to) {
        this.piece = piece;
        this.from = from;
        this.to = to;
    }
}
'''

class AlphaBetaNode:
    def __init__(self,piece,from_where,to_where):
        self.from_where=from_where   #int array(list)
        self.to_where=to_where       #int array(list)
        self.value=0                 #int
        self.piece=piece             #string 或者直接用int代号
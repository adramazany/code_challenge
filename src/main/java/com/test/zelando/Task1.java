package com.test.zelando;
/*
 * @created 1/23/2022 - 4:18 PM
 * @project code_challenge
 * @author adel.ramezani (adelramezani.jd@gmail.com)
 */

// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import com.test.lambda.LambdaExpression;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class Solution {
    Logger logger = LoggerFactory.getLogger(Solution.class);

    @Test
    void test_solution(){
        long t1 = System.currentTimeMillis();
        String[] B1= new String[]{"X.....>", "..v..X.", ".>..X..", "A......"};
        String[] B2= new String[]{"...Xv", "AX..^", ".XX.."};
        String[] B21= new String[]{
                  "...Xv...Xv...Xv"
                , "AX..^.X..^.X..^"
                , ".XX...XX...XX.."
                , "...Xv...Xv...Xv"
                , ".X..^.X..^.X..^"
                , ".XX...XX...XX.."
                , "...Xv...Xv...Xv"
                , ".X..^.X..^.X..^"
                , ".XX...XX...XX.."
        };
        String[] B3= new String[]{"...", ">.A"};
        String[] B4= new String[]{"A.v", "..."};

        assertThat(solution(B1)).isEqualTo(false);
        assertThat(solution(B2)).isEqualTo(true);
        assertThat(solution(B21)).isEqualTo(true);
        assertThat(solution(B3)).isEqualTo(false);
        assertThat(solution(B4)).isEqualTo(false);
        logger.info ("finished at {} ms.",(System.currentTimeMillis()-t1));
    }

    public boolean solution(String[] B) {
        // write your code in Java SE 8
        Board board = new Board(B,B.length-1,B[0].length()-1);

        if(board.isAssassianSeen()){
            return false;
        }

        return board.findFirstPath(board.getA_x(),board.getA_y());
    }




}

class Board{
    Logger logger = LoggerFactory.getLogger(Board.class);

    int exit_x;
    int exit_y;
    char[][] board;

    int N;
    int M;

    int A_x=-1;
    int A_y=-1;

    Set<String> seen=new HashSet();

    public Board(String[] B,int exit_x,int exit_y) {
        this.board = getBoard(B);
        this.exit_x=exit_x;
        this.exit_y=exit_y;

        fillGuardSeen();

        findAssassianLocation();
    }

    public boolean isAssassianSeen(){
        if(A_x==-1){
            return true;
        }
        return false;
    }

    public boolean findFirstPath(int x,int y){
        String pos = String.format("%d,%d",x,y);
        if(seen.contains(pos)){
            return false;
        }else{
            seen.add(pos);
        }
        logger.debug("findFirstPath {},{}",x, y);
        if(x==exit_x && y==exit_y){
            return true;
        }
        if(x>0 && board[x-1][y]=='.'){
            if(findFirstPath(x-1,y)) {
                return true;
            }
        }
        if(x<N-1 && board[x+1][y]=='.'){
            if(findFirstPath(x+1,y)) {
                return true;
            }
        }
        if(y<M-1 && board[x][y+1]=='.'){
            if(findFirstPath(x,y+1)) {
                return true;
            }
        }
        if(y>0 && board[x][y-1]=='.'){
            if(findFirstPath(x,y-1)) {
                return true;
            }
        }

        return false;
    }

    private void findAssassianLocation() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(board[i][j]=='A'){
                    A_x=i;
                    A_y=j;
                }
            }

        }
    }




    void fillGuardSeen(){
        this.N=board.length;
        this.M=board[0].length;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == '>') {
                    for (int k = j + 1; k < M; k++) {
                        if (board[i][k] == '.' || board[i][k] == 'A' || board[i][k] == 'S') {
                            board[i][k] = 'S';
                        } else {
                            break;
                        }
                    }
                } else if (board[i][j] == '<') {
                    for (int k = j - 1; k >= 0; k--) {
                        if (board[i][k] == '.' || board[i][k] == 'A' || board[i][k] == 'S') {
                            board[i][k] = 'S';
                        } else {
                            break;
                        }
                    }
                } else if (board[i][j] == 'v') {
                    for (int k = i + 1; k < N; k++) {
                        if (board[k][j] == '.' || board[k][j] == 'A' || board[k][j] == 'S') {
                            board[k][j] = 'S';
                        } else {
                            break;
                        }
                    }
                } else if (board[i][j] == '^') {
                    for (int k = i - 1; k >= 0; k--) {
                        if (board[k][j] == '.' || board[k][j] == 'A' || board[k][j] == 'S') {
                            board[k][j] = 'S';
                        } else {
                            break;
                        }
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) {
            logger.debug("fillGuardSeen:{}",board[i]);
        }
    }

    char[][] getBoard(String[] B){
        logger.debug("B={}, N={}, M={}",B,B.length,B[0].length());
        char[][] board = new char[B.length][B[0].length()];

        for (int i = 0; i < B.length; i++) {
            board[i] = B[i].toCharArray();
            logger.debug("board={}",board[i]);
        }
        return board;
    }

    public int getN() {
        return N;
    }

    public int getM() {
        return M;
    }

    public int getA_x() {
        return A_x;
    }

    public int getA_y() {
        return A_y;
    }
}

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(processInput(getInput(), true));
        System.out.println(processInput(getInput(), false));
    }
    private static int processInput(char[][] input, boolean part1) {
        var sum = 0;
        for(var i=0; i<input.length; i++){//traverse through each line
            for(var j=0; j<input[0].length; j++){
                if(part1 && !Pattern.matches("[0-9.]", String.valueOf(input[i][j]))){
                    sum += calculatePieces(input, i, j, true);
                }
                else if(!part1 && Pattern.matches("\\*", String.valueOf(input[i][j]))){
                    sum += calculatePieces(input, i, j, false);
                }
            }
        }
        return sum;
    }
        private static int calculatePieces(char[][] input, int row, int col, boolean part1) {
        var sum = part1 ? 0 : 1;
        var cnt = 0;
        int[] dx = {1, -1, 0, 0, 1, -1, 1, -1};
        int[] dy = {0, 0, 1, -1, 1, -1, -1, 1};

        for (var d = 0; d < 8; d++) {
            var newRow = row + dx[d];
            var newCol = col + dy[d];

            if (newRow >= 0 && newRow < input.length && newCol >= 0 && newCol < input[newRow].length) {
                var adjacentChar = input[newRow][newCol];
                var orCol = newCol;
                if (Character.isDigit(adjacentChar)) {
                    StringBuilder num = new StringBuilder(String.valueOf(adjacentChar));
                    input[newRow][newCol] = '.';
                    while(newCol + 1 < input.length && Character.isDigit(input[newRow][newCol+1])){
                        num.append(input[newRow][newCol + 1]);
                        input[newRow][newCol+1] = '.';
                        newCol++;
                    }
                    newCol = orCol;
                    while(newCol - 1 >= 0 && Character.isDigit(input[newRow][newCol-1])){
                        num.insert(0, input[newRow][newCol - 1]);
                        input[newRow][newCol-1] = '.';
                        newCol--;
                    }
                    if(part1)
                        sum+= Integer.parseInt(num.toString());
                    else {
                        sum *= Integer.parseInt(num.toString());
                        cnt++;
                    }
                }
            }
        }
            if(!part1 && cnt == 1)
                return 0;
        return sum;
    }




    public static char[][] getInput() throws FileNotFoundException {
        var reader = new Scanner(new File("C:\\Users\\USER\\IdeaProjects\\Advent2023\\src\\input3.txt"));
        var list = new ArrayList<String>();
        while (reader.hasNextLine())
            list.add(reader.nextLine());

        char[][] input = new char[list.size()][list.get(0).length()];

        for (var i = 0; i < list.size(); i++) {
            char[] chars = list.get(i).toCharArray();
            System.arraycopy(chars, 0, input[i], 0, chars.length);
        }

        return input;
    }
}

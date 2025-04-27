package test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.List;
import 

class Day2Test {

   //@org.junit.jupiter.api.Test
    @org.junit.Test
    public void testComputer() {
        Day2 myDay2 = new Day2();
        List<Integer> llist = List.of(1,0,0,0,99);
        int result1 = Day2.computer(llist,0,0);

        assertEquals(2, result1);
    }

    @org.junit.jupiter.api.Test
    void find_noun_verb() {
        List<Integer> inp = List.of(1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0);
        assertEquals(inp, 4259);
    }
}
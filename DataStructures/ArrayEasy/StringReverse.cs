using System;
using System.Collections.Generic;
using System.Text;

namespace ArrayEasy
{
    public class StringReverse
    {
        public static void ReverseRecursive(string word, int index)
        {
            if(index < 0)
            {
                return;
            }

            Console.Write(word[index]);
            ReverseRecursive(word, --index);
        }
    }
}

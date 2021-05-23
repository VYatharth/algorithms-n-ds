using System;

namespace InsertionSort
{
    class Program
    {
        static void Main(string[] args)
        {
            var array = new int[] { 2, 4, 3, 6, 1, 5, 8, 7 };
            var sortedArray = InsertionSort(array);

            foreach (var item in sortedArray)
            {
                Console.Write($" {item}");  
            }
        }

        static int[] InsertionSort(int[] array)
        {
            for (int i = 1; i < array.Length; i++)
            {
                var j = i-1;
                var num = array[i];
                while (j>-1 && array[j] > num)
                {
                    array[j+1] = array[j];
                    j--; 
                }

                array[j + 1] = num;
            }

            return array;
        }
    }
}

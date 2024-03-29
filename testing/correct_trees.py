CORRECT_TREE_1 = """    *
   ***
  *****
 *******
*********"""

CORRECT_TREE_2 = r"""    X
    ^
   /*\
  /***\
 /*****\
/*******\
   | |"""

CORRECT_TREE_3_1 = r"""    X
    ^
   /*\
  /*O*\
 /*O*O*\
/*O*O*O*\
   | |"""

CORRECT_TREE_3_2 = r"""    X
    ^
   /*\
  /*O*\
 /*****\
/*O*****\
   | |"""

CORRECT_POSTCARD = r"""--------------------------------------------------
|                                                |
|                                                |
|                                                |
|                                                |
|             X                                  |
|             ^                                  |
|            /*\                     X           |
|           /*O*\                    ^           |
|          /*O*O*\            X     /*\          |
|         /*O*O*O*\      X    ^    /*O*\         |
|        /*O*O*O*O*\     ^   /*\  /*****\        |
|       /*O*O*O*O*O*\   /*\ /*O*\/*O*****\       |
|      /*O*O*O*O*O*O*\ /*O*/*****\O*****O*\      |
|     /*O*O*O*O*O*O*O*\***/***O***\**O*****\     |
|    /*O*O*O*O*O*O*O*O*\|/*****O***\| |          |
|   /*O*O*O*O*O*O*OXO*O*/*****O*****\            |
|            | |   ^   /***O*******O*\           |
|                 /*\ /*******O*******\          |
|                /*O*\*O*******O*******\         |
|               /*****\      | |                 |
|              /***O***\                         |
|                 | |                            |
|                                                |
|                                                |
|                                                |
|                                                |
|                   Merry Xmas                   |
|                                                |
--------------------------------------------------"""
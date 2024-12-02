from colorist import Color
import platform

def define_ascii():
    lines = []
    if platform.system() == "Windows":
        lines = [
            f"{Color.BLUE}                    ....,,:;+ccllll  {Color.OFF}",
            f"{Color.BLUE}     ...,,+:;  clllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE},cclllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}                                     {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}`'ccllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}      `' ''*::  :ccllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}                      ````'' *::cll  {Color.OFF}"
        ]
    elif platform.system() == "Linux":
        lines = [
            f"{Color.BLACK}            a8888b.         {Color.OFF}",
            f"{Color.BLACK}          d888888b.         {Color.OFF}",
            f"{Color.BLACK}          8P'YP'Y88         {Color.OFF}",
            f"{Color.BLACK}          8|{Color.OFF}{Color.WHITE}O{Color.OFF}{Color.BLACK}||{Color.OFF}{Color.WHITE}O{Color.OFF}{Color.BLACK}|88         {Color.OFF}",
            f"{Color.BLACK}          8{Color.OFF}{Color.YELLOW}'    .{Color.OFF}{Color.BLACK}88         {Color.OFF}",
            f"{Color.BLACK}          8{Color.OFF}{Color.YELLOW}`._.'{Color.OFF}{Color.BLACK} Y8.        {Color.OFF}",
            f"{Color.BLACK}        d/      `8b.        {Color.OFF}",
            f"{Color.BLACK}      .dP   .     Y8b.      {Color.OFF}",
            f"{Color.BLACK}      d8:'   '   `::88b.    {Color.OFF}",
            f"{Color.BLACK}     d8'           `Y88b    {Color.OFF}",
            f"{Color.BLACK}    :8P     '       :888    {Color.OFF}",
            f"{Color.BLACK}     8a.    :      _a88P    {Color.OFF}",
            f"{Color.BLACK}   {Color.OFF}{Color.YELLOW}._/'Y{Color.OFF}{Color.BLACK}aa_     :.{Color.OFF}{Color.YELLOW} -----    {Color.OFF}",
            rf"{Color.BLACK}   {Color.OFF}{Color.YELLOW}\    YP'      `{Color.OFF}{Color.YELLOW}|     `.  {Color.OFF}",
            rf"{Color.BLACK}   {Color.OFF}{Color.YELLOW}/     \.{Color.OFF}{Color.BLACK}_____.d{Color.OFF}{Color.YELLOW}|    {Color.OFF}{Color.YELLOW} .'  {Color.OFF}",
            f"{Color.BLACK}   {Color.OFF}{Color.YELLOW}`--..__){Color.OFF}{Color.BLACK}888888P{Color.OFF}{Color.YELLOW}`._.'     {Color.OFF}",
            f"{Color.BLACK}                            {Color.OFF}",
            f"{Color.BLACK}                            {Color.OFF}"
        ]
    elif platform.system() == "Darwin":
        lines = [

            f"{Color.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀{Color.OFF}",
            f"{Color.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠀⠀⠀⠀⠀⠀{Color.OFF}"
            f"{Color.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀{Color.OFF}"
            f"{Color.RED}⠀⠀⠀⢀⣠⣤⣤⣤⣀⣀⠈⠋⠉⣁⣠⣤⣤⣤⣀⡀⠀⠀{Color.OFF}"
            f"{Color.RED}⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀{Color.OFF}"
            f"{Color.RED}⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀{Color.OFF}"
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀{Color.OFF}"
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀{Color.OFF}"
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀{Color.OFF}"
            f"{Color.RED}⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀{Color.OFF}"
            f"{Color.RED}⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁{Color.OFF}"
            f"{Color.RED}⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀{Color.OFF}"
            f"{Color.RED}⠀⠀⠀⠈⠙⢿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⡿⠋⠀⠀⠀{Color.OFF}"
            f"{Color.RED}                          {Color.OFF}"
            f"{Color.RED}                          {Color.OFF}"
            f"{Color.RED}                          {Color.OFF}"
            f"{Color.RED}                          {Color.OFF}"
            f"{Color.RED}                          {Color.OFF}"
        ]
    return lines
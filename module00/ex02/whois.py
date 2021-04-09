# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kaye <kaye@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/09 17:03:19 by kaye              #+#    #+#              #
#    Updated: 2021/04/09 17:54:34 by kaye             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
	if len(sys.argv) == 1:
		exit()
	else:
		exit(print('ERROR'))

try:
	av = int(sys.argv[1])
except ValueError:
	print('ERROR')
else:
	if av == 0:
		print("I'm Zero.")
	elif av % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Old")

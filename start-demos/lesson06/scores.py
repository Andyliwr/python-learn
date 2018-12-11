#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：计算分数
student_num = int(input('请输入学生数量: '))
student_name, physics_score, maths_score, history_score = '', 0, 0, 0
all_scores = []
for i in range(student_num):
  student_name = input('请输入第 {} 个学生的姓名: '.format(i+1))
  physics_score = float(input('请输入 {} 的物理成绩: '.format(student_name)))
  maths_score = float(input('请输入 {} 的数学成绩: '.format(student_name)))
  history_score = float(input('请输入 {} 的历史成绩: '.format(student_name)))
  this_student = {'student_name': student_name, 'physics_score': physics_score, 'maths_score': maths_score, 'history_score': history_score}
  all_scores.append(this_student)
# 开始处理学生成绩
for i in range(student_num):
  total_score = float(all_scores[i]['physics_score'] + all_scores[i]['maths_score'] + all_scores[i]['history_score'])
  print('{} 的总成绩: {}'.format(all_scores[i]['student_name'], total_score))
  if total_score > 120:
    is_pass = all_scores[i]['student_name'] + ' 通过:)'
  else:
    is_pass = all_scores[i]['student_name'] + ' 未通过:('
  print('{} 的总成绩: {}'.format(all_scores[i]['student_name'], is_pass))
def list names
  res = ''
  if names.length <= 0
    return ''
  end
  if names.length == 1
    return names[0][:name]
  end
  for i in 0..names.length - 3
    puts i
    puts names[i][:name]
    res = res + names[i][:name] + ", "
  end
  res = res + names[names.length - 2][:name] + " & " + names[names.length - 1][:name]
end

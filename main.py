import numpy as np

class Stack: 
      def __init__(self, recipient):
            self.recipient = recipient # Important to make the recipient an attribute of the class for referencing all throughout the code
            self.original = recipient
            self.count_updates = 0 
            self.__background_work() # Create document as soon as class is instantiated
      def __background_work(self):
            with open("updates_stack.txt", "w") as file: # Should clean up the txt from prior appends
                  file.write("UPDATES REGISTRER: STACK\n")
                  file.write("-"*60)
                  file.close()
      def get_out(self): 
            recipient = self.recipient
            before_change = self.recipient
            value_out = recipient[-1]
            self.recipient = recipient[:-1] # Should display the stack without the last one
            recipient = self.recipient
            self.count_updates += 1
            current_count_value = self.count_updates
            with open("updates_stack.txt", "a") as file:
                  file.write(f"\nUpdate nº: {current_count_value} / GET_OUT")
                  file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                  file.write(f"\n\tMethod used 'get_out'")
                  file.close()
            return recipient, value_out
      def get_out_by_index(self, index): # Get out by index; not practical 
            recipient = self.recipient
            before_change = self.recipient
            value_out = recipient[index]
            legal_value_out = recipient[-1]
            if value_out == legal_value_out: # If index is legal
                  self.recipient = recipient[:index] # Updating
                  recipient = self.recipient   # Storing updated array version  
                  self.count_updates += 1    
                  current_count_value =self.count_updates
                  with open("updates_stack.txt", "a") as file:
                        file.write(f"\nUpdate nº: {current_count_value} / GET_OUT_BY_INDEX")
                        file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                        file.write(f"\n\tMethod used 'get_out_by_index' with index {index}")
                        file.close()
                  return recipient, value_out
            else:
                  print(f"{self.recipient[index]} is not the last element in the stack. Try again!")  
                  return f"List is {self.recipient}"         
      def get_add(self, value):
            recipient = self.recipient[:] # Copy because if not before_change will not store properly the its original shape (being affected after the append )
            before_change = self.recipient # Gets the value stored at that moment in the attribute; not affect by next updates
            recipient.append(value)
            self.recipient = recipient # Update the receipe with the add 
            recipient = self.recipient # Accessing the updated stack
            self.count_updates += 1
            current_count_value = self.count_updates
            with open("updates_stack.txt", "a") as file:
                        file.write(f"\nUpdate nº: {current_count_value} / GET_ADD")
                        file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                        file.write(f"\n\tMethod used 'get_add' with added element {value}")
                        file.close()
            return recipient
      """ ALL METHODS BELOW DO NOT MUTATE THE STACK; THEY JUST PROVIDE METADATA"""
      def get_stack(self):
            return f" Stack is {self.recipient}"
      def get_size(self):
            return len(self.recipient)
      def get_content_bool(self):
            if self.recipient:
                  return f"Not empty {self.recipient}"
            else:
                  return f"Empty {self.recipient}"
      def get_comparasion(self):
            if self.original == self.recipient:
                  return (f"The list is the same! {self.recipient}")
            else:
                  return (f"The list has changed!:\n\tOriginal list is:  {self.original} \n\tCurrent list is: {self.recipient}")
      def get_n_updates(self):
            return self.count_updates
            
      
class Queue: # First in first out
      def __init__(self, recipient):
            self.recipient = recipient # Important to make the recipient an attribute of the class for referencing all throughout the code
            self.original = recipient
            self.count_updates = 0
            self.__background_work()
      def __background_work(self):
            with open("updates_queue.txt", "w") as file: # Should clean up the txt from prior appends
                  file.write("UPDATES REGISTRER: QUEUE\n")
                  file.write("-"*60)
                  file.close()
      def get_out(self): 
            recipient = self.recipient
            before_change = self.recipient
            value_out = recipient[0]
            self.recipient = recipient[1:] # Should display the stack without the last one
            recipient = self.recipient
            self.count_updates += 1
            current_count_value = self.count_updates
            with open("updates_queue.txt", "a") as file:
                  file.write(f"\nUpdate nº: {current_count_value} / GET_OUT")
                  file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                  file.write(f"\n\tMethod used 'get_out'")
                  file.close()
            return recipient, value_out
      def get_out_by_index(self, index): # Get out by index; not practical 
            recipient = self.recipient
            before_change = self.recipient
            value_out = recipient[index]
            legal_value_out = recipient[0]
            if value_out == legal_value_out: # If index is legal
                  self.recipient = recipient[:index] # Updating
                  recipient = self.recipient   # Storing updated array version  
                  self.count_updates += 1    
                  current_count_value =self.count_updates
                  with open("updates_queue.txt", "a") as file:
                        file.write(f"\nUpdate nº: {current_count_value} / GET_OUT_BY_INDEX")
                        file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                        file.write(f"\n\tMethod used 'get_out_by_index' with index {index}")
                        file.close()
                  return recipient, value_out
            else:
                  print(f"{self.recipient[index]} is not the first element in the stack. Try again!")  
                  return f"List is {self.recipient}"         
      def get_add(self, value):
            recipient = self.recipient[:] # Copy because if not before_change will not store properly the its original shape (being affected after the append )
            before_change = self.recipient # Gets the value stored at that moment in the attribute; not affect by next updates
            recipient.append(value)
            self.recipient = recipient # Update the receipe with the add 
            recipient = self.recipient # Accessing the updated stack
            self.count_updates += 1
            current_count_value = self.count_updates
            with open("updates_queue.txt", "a") as file:
                        file.write(f"\nUpdate nº: {current_count_value} / GET_ADD")
                        file.write(f"\n\tStack before {before_change}, stack now {recipient}")
                        file.write(f"\n\tMethod used 'get_add' with added element {value}")
                        file.close()
            return recipient
      """ ALL METHODS BELOW DO NOT MUTATE THE STACK; THEY JUST PROVIDE METADATA"""
      def get_stack(self):
            return f" Stack is {self.recipient}"
      def get_size(self):
            return len(self.recipient)
      def get_content_bool(self):
            if self.recipient:
                  return f"Not empty {self.recipient}"
            else:
                  return f"Empty {self.recipient}"
      def get_comparasion(self):
            if self.original == self.recipient:
                  return (f"The list is the same! {self.recipient}")
            else:
                  return (f"The list has changed!:\n\tOriginal list is:  {self.original} \n\tCurrent list is: {self.recipient}")
      def get_n_updates(self):
            return self.count_updates
      

x = Queue([1,2,3,4,5])

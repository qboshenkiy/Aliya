import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        total_price = product.price * quantity
        for existing_item in self.items:
            if existing_item['product'] == product:
                existing_item['quantity'] += quantity
                existing_item['total_price'] += total_price
                return
        self.items.append({'product': product, 'quantity': quantity, 'total_price': total_price})

    def remove_product(self, product, quantity):
        for existing_item in self.items:
            if existing_item['product'] == product:
                if existing_item['quantity'] <= quantity:
                    self.items.remove(existing_item)
                else:
                    existing_item['quantity'] -= quantity
                    existing_item['total_price'] -= product.price * quantity
                return

    def calculate_total(self):
        return sum(item['total_price'] for item in self.items)

class StoreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Магазин")

        self.product_list = [
            Product("Айфон", 1000.0),
            Product("Мак бук", 2000.0),
            Product("Тесла", 30000.0),
        ]

        self.shopping_cart = ShoppingCart()

        self.product_label = tk.Label(master, text="Выберите продукт:")
        self.product_label.pack()

        self.product_var = tk.StringVar(master)
        self.product_var.set(self.product_list[0].name)

        self.product_menu = tk.OptionMenu(master, self.product_var, * [product.name for product in self.product_list])
        self.product_menu.pack()

        self.quantity_label = tk.Label(master, text="Выберите количество:")
        self.quantity_label.pack()

        self.quantity_spinbox = tk.Spinbox(master, from_=1, to=10)
        self.quantity_spinbox.pack()

        self.add_to_cart_button = tk.Button(master, text="Добавить в корзину", command=self.add_to_cart)
        self.add_to_cart_button.pack()

        self.remove_from_cart_button = tk.Button(master, text="Удалить из корзины", command=self.remove_from_cart)
        self.remove_from_cart_button.pack()

        self.show_cart_button = tk.Button(master, text="Показать корзину", command=self.show_cart)
        self.show_cart_button.pack()

    def add_to_cart(self):
        selected_product_name = self.product_var.get()
        selected_product = next((product for product in self.product_list if product.name == selected_product_name), None)

        if selected_product:
            quantity = int(self.quantity_spinbox.get())
            self.shopping_cart.add_product(selected_product, quantity)
            messagebox.showinfo("Успех", f"{quantity} {selected_product.name}(ов) добавлено в корзину.")
        else:
            messagebox.showerror("Ошибка", "Выберите корректный продукт.")

    def remove_from_cart(self):
        selected_product_name = self.product_var.get()
        selected_product = next((product for product in self.product_list if product.name == selected_product_name), None)

        if selected_product:
            quantity = int(self.quantity_spinbox.get())
            self.shopping_cart.remove_product(selected_product, quantity)
            messagebox.showinfo("Успех", f"{quantity} {selected_product.name}(ов) удалено из корзины.")
        else:
            messagebox.showerror("Ошибка", "Выберите корректный продукт.")

    def show_cart(self):
        cart_content = "\n".join([f"{item['product'].name} (x{item['quantity']}): {item['total_price']}" for item in self.shopping_cart.items])
        total_price = self.shopping_cart.calculate_total()

        messagebox.showinfo("Корзина", f"Содержимое корзины:\n{cart_content}\n\nОбщая стоимость: {total_price}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()

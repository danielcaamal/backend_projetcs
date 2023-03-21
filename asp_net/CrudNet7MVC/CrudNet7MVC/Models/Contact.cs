using System.ComponentModel.DataAnnotations;

namespace CrudNet7MVC.Models
{
    public class Contact
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "The field {0} is required")]
        public string Name { get; set; } = string.Empty;

        [Required(ErrorMessage = "The field {0} is required")]
        public string Email { get; set; } = string.Empty;
        
        [Required(ErrorMessage = "The field {0} is required")]
        public string Phone { get; set; } = string.Empty;

        [Required(ErrorMessage = "The field {0} is required")]
        public string CellPhone { get; set; } = string.Empty;

        [Required(ErrorMessage = "The field {0} is required")]
        public DateTime CreatedAt { get; set; } = DateTime.Now;

    }
}
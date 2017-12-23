#!/usr/local/bin/gosh
(define (read-file file-name)
  (call-with-input-file "example.fasta" port->string-list))

(define (main args)
  (let* ((file-name "example.fasta")
         (lst (read-file file-name))
         (sequence (apply string-append (cdr lst))))
    (let* ((count-ATGC-list
             (lambda (lst)
               (let loop ((num-A 0) (num-T 0) (num-G 0) (num-C 0) (l lst))
                 (if (null? l)
                   (list num-A num-T num-G num-C)
                   (let ((c (car l)))
                     (cond ((equal? c #\A) (loop (+ num-A 1) num-T num-G num-C (cdr l)))
                           ((equal? c #\T) (loop num-A (+ num-T 1) num-G num-C (cdr l)))
                           ((equal? c #\G) (loop num-A num-T (+ num-G 1) num-C (cdr l)))
                           ((equal? c #\C) (loop num-A num-T num-G (+ num-C 1) (cdr l)))
                           (#t "error")))))))
           (count-ATGC (lambda (sequence) (count-ATGC-list (string->list sequence)))))
      (let* ((result (count-ATGC sequence))
             (message (if (list? result)
                        (apply string-append
                               (apply append (map list
                                                  (list "A: " " T: " " G: " " C: ")
                                                  (map number->string (count-ATGC sequence)))))
                        result)))
        (display message)
        (newline)
        )
      )
    )
  0
  )

